
# Hashnode_Py

**hashnode_py** is a Python package designed to interact with the Hashnode GraphQL API. With this package, you have the ability to publish, update, or delete your articles and drafts. Additionally, it offers various functionalities to seamlessly interact with your publication directly from your code.

## Features

- Publish, Update, and Delete Articles/Drafts
- Get your hashnode data including: posts, publications, followers, subscriptions and many more
- Access your feed posts and apply filters 


## Installation

**Install hashnode_py with pip**

First Install Dependencies:
```bash
  pip install gql requests requests-toolbelt
  ```
Then download the package
```bash
  pip install hashnode-py
```
    
## Usage/Examples

First get your Hashnode Personal Access Token from [here](https://hashnode.com/settings/developer) 

Then jump in to your code 
```python
from hashnode_py import HashnodeClient

client = HashnodeClient("...ad0a")
```
### Publish New Article

```python
publication = client.get_publication("<YOUR_BLOG_DOMAIN_NAME>")

print(publication.publish_post(
            title="this is test title",
            content="this is a test content",
            tags_slug=[{"slug": "test", "name": "Test"}]
        ))
```
The message will be displayed indicating that the post has been successfully published, along with the post's ID.

### Update The Article
```python
post_id = "POST_ID"

print(publication.update_post(post_id=post_id, title="[UPDATE] this is test title"))
```
The message will be displayed indicating that the post has been successfully updated, along with the post's ID.

### Delete The Article
```python
print(publication.remove_post(post_id=post_id))
```
The message will be displayed indicating that the post has been successfully removed, along with the post's ID.

### Publish Draft
```python
draft = publication.get_drafts()[0]

print(publication.publish_draft(draft_id=draft.id))
```
The message will be displayed indicating that the draft has been successfully published, along with the post's ID.



## License

[MIT](https://choosealicense.com/licenses/mit/)


## Contributing

Contributions are always welcome!


