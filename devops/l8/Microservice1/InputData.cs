using System.ComponentModel.DataAnnotations;

public record InputData(
    [Required] string Name,
    [Range(1, 100)] int Age,
    [EmailAddress] string Email
);
