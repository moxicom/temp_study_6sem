// Program.cs
using Microsoft.EntityFrameworkCore;
var builder = WebApplication.CreateBuilder(args);
// Add DB Context service
builder.Services.AddDbContext<AppDbContext>(options =>
options.UseNpgsql(builder.Configuration.GetConnectionString("DefaultConnection")));
var app = builder.Build();

using (var scope = app.Services.CreateScope())
{
    var db = scope.ServiceProvider.GetRequiredService<AppDbContext>();
    db.Database.EnsureCreated();
}

// API endpoint
app.MapPost("/api/data", async (InputData data, AppDbContext db) =>
{
    await db.DataRecords.AddAsync(new DataRecord
    {
        Name = data.Name,
        Age = data.Age,
        Email = data.Email,
        ReceivedAt = DateTime.UtcNow
    });
    await db.SaveChangesAsync();
    return Results.Ok("Data saved successfully");
});
app.Run();