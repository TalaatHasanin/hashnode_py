user_info = """
query User($username: String!) 
{
  user(username: $username) 
  {
    id
    username
    name
    bio {text}
    profilePicture
    followersCount
    followingsCount
    tagline
    dateJoined
    location
    availableFor
    deactivated
    following
    followsBack
    isPro
  }
}
"""
social_media = """
query User($username: String!) 
{
  user(username: $username) 
  {
    socialMediaLinks {
      website
      github
      twitter
      instagram
      facebook
      stackoverflow
      linkedin
      youtube
    }
  }
}
"""

badges = """
query User($username: String!) 
{
  user(username: $username) 
  {
    badges {
      id
      name
      description
      image
      dateAssigned
      infoURL
      suppressed
    }
  }
}
"""

publications = """
query User($username: String!) 
{
  user(username: $username) 
  {
    publications(first: 10){
      edges{
        node{
          id
          title
          displayTitle
          descriptionSEO
          about{text}
          url
          author{username}
          headerColor
          integrations{gaTrackingID}
          followersCount
          pinnedPost{id}
        }
        role
      }
    }
  }
}
"""

posts = """
query User(
  $username: String!
  $page_size: Int!
  $page: Int!
) 
{
  user(username: $username) 
  {
    posts(
      pageSize: $page_size
      page: $page
    ){
      nodes{
        id
        slug
        title
        subtitle
        author{username}
        url
        publication{title}
        cuid
        coverImage{url}
        brief
        readTimeInMinutes
        views
        reactionCount
        responseCount
        featured
        bookmarked
        featuredAt
        publishedAt
        updatedAt
        isFollowed
        content{markdown}
      }
    }
  }
}
"""

tags_following = """
query User(
  $username: String!
) 
{
  user(username: $username) 
  {
    tagsFollowing{
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
}
"""

