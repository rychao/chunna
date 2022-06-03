variable "gcp_project" {
  description = "Name of the GCP project"
  type        = string
  default     = "cse155"
}

variable "gcp_region" {
  description = "Region to host gcp resources"
  type        = string
  default     = "us-west1"
}

variable "machine_type" {
  description = "Desired machine type of instance"
  type        = string
  default     = "e2-medium"
}
