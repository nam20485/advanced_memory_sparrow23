var builder = DistributedApplication.CreateBuilder(args);

var apiService = builder.AddProject<Projects.AdvancedMemory_AppHost_ApiService>("apiservice");

builder.AddProject<Projects.AdvancedMemory_AppHost_Web>("webfrontend")
    .WithExternalHttpEndpoints()
    .WithReference(apiService);

builder.Build().Run();
