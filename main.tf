terraform {
  required_version = ">= 0.12"
}

provider "google" {
  # credentials = var.gcp_credentials
  project      = "PROJECT_NAME"
  region       = "us-west1"

}

module "instance" {
  source = "./modules/instance"
  instance_name = "chuck"
  gcp_zone = "us-west1-b"
  machine_type = "n1-standard-1" # default is e2-medium
  image = "ubuntu-os-cloud/ubuntu-1804-lts"
}

# configure google instance
# resource "null_resource" "configure-gce-instance" {
#   depends_on = [
#     google_compute_instance.priceScraper
#   ]
# }
