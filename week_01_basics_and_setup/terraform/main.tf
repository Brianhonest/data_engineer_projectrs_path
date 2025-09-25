terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "7.4.0"
    }
  }
}

provider "google" {
  # Configuration options
  project = "lunar-box-472914-f7"
  region  = "us-central1"
}

resource "google_storage_bucket" "auto-expire" {
  name          = "lunar-box-472914-f7-terraform-demo"
  location      = "US"
  force_destroy = true


  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}