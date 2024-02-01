tag_info = """
query Tag(
  $slug: String!
){
  tag(slug: $slug){
    id
    name
    slug
    logo
    tagline
    info{text}
    followersCount
    postsCount
  }
}
"""