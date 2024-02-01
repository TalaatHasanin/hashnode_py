publication_info = """
query Publication(
  $id: ObjectId,
  $host: String
) {
  publication(
    id: $id,
    host: $host
  ) {
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
}
"""

drafts = """
query Publication(
  $id: ObjectId
  $first: Int!
) {
  publication(
    id: $id
  ) {
    drafts(first: $first){
      edges{
        node{
          id
          slug
          title
          subtitle
          author{username}
          coverImage{url}
          readTimeInMinutes
          content{text}
          updatedAt
          lastBackup{
            status
            at
          }
          lastSuccessfulBackupAt
          lastFailedBackupAt
        }
      }
    }
  }
}
"""