post_info = """
query Post(
  $id: ID!
) {
  post(
    id: $id,
  ) {
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
"""

comments = """
query GetComments(
  $id: ID!
  $first: Int!
) {
  post(
    id: $id,
  ) {
    comments(
      first: $first
    ){
      edges{
        node{
          id
          content{text}
          author{username}
          dateAdded
          stamp
          totalReactions
          myTotalReactions
        }
      }
    }
  }
}
"""

feed = """
query Feed(
  $first: Int!
  $type: FeedType
  $minReadTime:  Int
  $maxReadTime: Int
  $tags: [ObjectId!]
){
  feed(
    first: $first
    filter: {
      type: $type
      minReadTime: $minReadTime
      maxReadTime: $maxReadTime
      tags: $tags
    }
  ){
    edges{
      node{
        id
        title
        slug
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