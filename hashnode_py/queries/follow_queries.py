follows_info = """
query Follows(
  $username: String!
  $pageSize: Int!
  $page: Int!
) 
{
  user(username: $username) 
  {
    follows(
      pageSize: $pageSize, 
      page: $page
    ) {
      nodes{
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
      pageInfo {
        hasNextPage,
        hasPreviousPage,
        previousPage,
        nextPage
      }
    }
  }
}
"""

followers_info = """
query Followers(
  $username: String!
  $pageSize: Int!
  $page: Int!
) 
{
  user(username: $username) 
  {
    followers(
      pageSize: $pageSize, 
      page: $page
    ) {
      nodes{
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
      pageInfo {
        hasNextPage,
        hasPreviousPage,
        previousPage,
        nextPage
      }
    }
  }
}
"""