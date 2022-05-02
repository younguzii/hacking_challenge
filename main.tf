data "external" "external_provider" {
  program = ["python", "${path.module}/bad_python.py"]
}

output "external_provider_example" {
  value = data.external.external_provider
}
