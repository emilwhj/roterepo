using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace csharpExperiment
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            var apiInstance = new DefaultApi();
            try
            {
                apiInstance.compactGet(0, 65, 12);
            }
            catch(Exception e)
            {
                Debug.Print("Exception when calling defaultapi: " + e.Message);
            }
        }
    }
}
