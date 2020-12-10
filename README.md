# git_peaker
A small Flask application that interacts with github.

## Environment parameters
* `GITHUB_API_KEY`: your GitHub access key. Neccessary for using github graphql api. you can get your key [here](https://github.com/settings/tokens).

## Install & run
Download
```bash
git clone https://github.com/erayozer17/git_peaker.git
```
and run
```make run```

the app will be running on ```localhost:5001```

## Local testing
Code linting
```make lint```

Run the tests
```make test```

## Endpoints
```http
GET /active/<username>
```
| parameter | type | description |
| :--- | :--- | :--- |
| `username` | `string` | **Required**. The username of the user you want to see the info about. |

### Response
if the user has pushed code to any repo within the last 24h, returns `true`, otherwise `false`.
```javascript
{
    "is_active_since_yesterday": bool
}

```
---
```http
GET /downwards/<repo>
```
| parameter | type | description |
| :--- | :--- | :--- |
| `repo` | `string` | **Required**. The GitHub repository to question. |

### Response
if more code got deleted from the repo than added, returns `true`, otherwise `false`.
```javascript
{
    "is_repo_downwarded_since_last_week": bool
}
```
