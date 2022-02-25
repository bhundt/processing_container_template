# Template for a processing job for DIY-ML-P
test
## Usage
- **Build**: `docker build -t processing_job:0.0.1 .`
- **Run**: `docker run --name "processing_job" --rm -v :/data -v :/feature-store processing_job:0.0.1`