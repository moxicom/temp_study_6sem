// // Program.cs
// using Microsoft.EntityFrameworkCore;
// var builder = WebApplication.CreateBuilder(args);
// // Add DB Context service
// builder.Services.AddDbContext<AppDbContext>(options =>
// options.UseNpgsql(builder.Configuration.GetConnectionString("DefaultConnection")));
// var app = builder.Build();

// // API endpoint
// app.MapPost("/api/data", async (InputData data, AppDbContext db) =>
// {
//     await db.DataRecords.AddAsync(new DataRecord
//     {
//         Name = data.Name,
//         Age = data.Age,
//         Email = data.Email,
//         ReceivedAt = DateTime.UtcNow
//     });
//     await db.SaveChangesAsync();
//     return Results.Ok("Data saved successfully");
// });
// app.Run();

using Microsoft.EntityFrameworkCore;
using System.Net.Http.Json;
using Microsoft.AspNetCore.Mvc;
using System.Text.Json;
using System.Net.Http;
using System.Net.Http.Formatting;

var builder = WebApplication.CreateBuilder(args);

// Add HttpClientFactory service
builder.Services.AddHttpClient("Microservice2Client", client =>
{
    client.BaseAddress = new Uri("http://microservice2:8000/");
});

var app = builder.Build();

app.MapPost("/api/data", async (InputData data, IHttpClientFactory httpClientFactory) =>
{
    try
    {
        // Create HttpClient using the factory
        using HttpClient httpClient = httpClientFactory.CreateClient("Microservice2Client");
        
        // Send request
        var response = await httpClient.PostAsJsonAsync("api/process", data);
        
        if (!response.IsSuccessStatusCode)
        {
            return Results.Problem(
                detail: $"Microservice2 error: {response.StatusCode}",
                statusCode: (int)response.StatusCode);
        }
        
        return Results.Ok("Data sent successfully");
    }
    catch (Exception ex)
    {
        return Results.Problem(
            detail: ex.Message,
            statusCode: StatusCodes.Status500InternalServerError);
    }
});

app.Run();