# Serverless Python Sample
[![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)

A simple serverless python sample. The service is running on AWS Lambda using [Serverless Framework](https://github.com/serverless/serverless).

The service has a dependency on external package (`requests`) and it exposes 2 REST API endpoints:

| **Endpoint** |**Description**|
|-------|------|
| `GET /posts` | Retrieves a list of posts  |
| `GET /posts/{id}` | Retrieves a specific post (e.g. `GET /posts/5`) |


# Usage
## Setup
| **Step** | **Command** |**Description**|
|---|-------|------|
|  1. | `npm install -g serverless` | Install Serverless CLI  |
|  2. | Set up an AWS account with admin permissions | [Documentation](https://github.com/serverless/serverless/blob/master/docs/02-providers/aws/01-setup.md)  |

## Development
| **Step** | **Command** |**Description**|
|---|-------|------|
|  1. | `mkvirtualenv posts` | Create virtual environment |
|  2. | `pip install -r requirements.txt` | Install dependencies|


## Deployment
Create dependencies folder for packaging

    pip install -t vendored -r requirements.txt

And... deploy!
 
	sls deploy
	
### Invocation
You can trigger a function: 

	# Invoke function without input
	sls invoke -f listposts
	
	# Provide input
	sls invoke -f getpost -p event.json
	
or

	curl <host>/posts
	curl <host>/posts/5

# Tips & Tricks

### `help` command
Just use it on anything:

	sls  help
or

	sls <command> --help

### `deploy function` command
Deploy only one function:

	sls deploy function -f <function-name>

### `logs` command
Tail the logs of a function:

	sls logs -f <function-name> -t

### `info` command
Information about the service (stage, region, endpoints, functions):

	sls info

### `invoke` command
Run a specific function with a provided input and get the logs

	sls invoke -f <function-name> -p event.json -l

# Credits
[JSONPlaceholder](https://jsonplaceholder.typicode.com) by [@typicode](https://github.com/typicode) is used for the posts backend.