# Small demo with AWS, python and boto

## Prerequisities

Inside the *docker* folder, create *env_files* folder and create a file called *aws_cred.env*. The file should have the following structure:

```bash
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=
```

Fill out the values accordingly.

## Create Docker container

### Step into docker folder

```bash
cd docker
```

### Build image

 ```bash
docker build . --tag=boto3-image
```

### Run container

```bash
docker run -itd --rm --name aws-boto3 --hostname aws-boto3 -v C:\marko\GitHub\aws-boto3-python\test_files:/aws-boto3-python --env-file "env_files/aws_cred.env" boto3-image
```

Make sure you map to the folder you cloned the repository to.

### Enter the container

```bash
docker exec -it aws-boto3 bash
```

## Once in the container

The file *ec2.py* will execute the boto library and manipulate with the instances in AWS. Check the AWS Console if the code is working correctly.

I am using Python library *click* to use options at script execution. The following options are available:

* dry_run - give value False when running option *state* Launch
* instance_id - use when running state Start, Stop, Reboot or Terminate
* state - following instance states are available: Launch, Start, Stop, Reboot or Terminate

Make sure to delete the volumes manually once you terminate the instances.
