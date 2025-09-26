variable "credentials" {
    description = "My Credentials"
    default = "./keys/my-creds.json"
}

variable "project_id" {
  description = "Project"
  default     = "lunar-box-472914-f7"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}
variable "location" {
  description = "Project Location"
  default     = "US"
}
variable "bq_dataset_namer" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "GCS Bucket Name"
  default     = "lunar-box-472914-f7-terraform-demo"

}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}