toggle_follow = """
mutation ToggleFollow(
  $username: String
){
  toggleFollowUser(
    username: $username
  ){
    user{
      username: username
      following
    }
  }
}
"""

like_post = """
mutation LikePost(
  $postId: ID!
  $likesCount: Int
){
  likePost(
    input:{
      postId: $postId
      likesCount: $likesCount
    }
  ){
    post{
      id
      title
    }
  }
}
"""

publish_post = """
mutation PublishPost(
  $title: String!
  $subtitle: String
  $publicationId: ObjectId!
  $content: String!
  $imageUrl: String
  $slug: String
  $originUrl: String
  $tags: [PublishPostTagInput!]!
  $disableComments: Boolean
  $publishAs: ObjectId
  $seriesId: ObjectId
  $settings: PublishPostSettingsInput
  $coAuthors: [ObjectId!]

){
  publishPost(
    input: {
      title: $title
      subtitle: $subtitle
      publicationId: $publicationId
      contentMarkdown:$content
      coverImageOptions: {
        coverImageURL: $imageUrl
      }
      slug: $slug
      originalArticleURL: $originUrl
      tags: $tags
      disableComments: $disableComments
      publishAs: $publishAs
      seriesId: $seriesId
      settings: $settings
      coAuthors: $coAuthors
    }
  ){
    post{
      id
    }
  }
}
"""

update_post = """
mutation UpdatePost(
  $postId: ID!
  $title: String
  $subtitle: String
  $publishedAt: DateTime
  $content: String
  $imageUrl: String
  $slug: String
  $originUrl: String
  $tags: [PublishPostTagInput!]
  $publishAs: ObjectId
  $seriesId: ObjectId
  $settings: UpdatePostSettingsInput
  $coAuthors: [ObjectId!]
  $publicationId: ObjectId
){
  updatePost(
    input: {
      id: $postId
      title: $title
      subtitle: $subtitle
      contentMarkdown:$content
      publishedAt: $publishedAt
      coverImageOptions: {
        coverImageURL: $imageUrl
      }
      slug: $slug
      originalArticleURL: $originUrl
      tags: $tags
      publishAs: $publishAs
      seriesId: $seriesId
      settings: $settings
      coAuthors: $coAuthors
      publicationId: $publicationId
    }
  ){
    post{
      id
    }
  }
}
"""

remove_post = """
mutation RemovePost(
  $postId: ID!
){
  removePost(
    input: {
      id: $postId
    }
  ){
    post{
      id
    }
  }
}
"""

like_comment = """
mutation LikeComment(
  $commentId: ID!
  $likesCount: Int
){
  likeComment(
    input: {
      commentId: $commentId
      likesCount: $likesCount
    }
  ){
    comment{
      author{username}
    }
  }
}
"""

add_comment = """
mutation AddComment(
  $postId: ID!
  $content: String!
){
  addComment(
    input: {
      postId: $postId
      contentMarkdown: $content
    }
  ){
    comment{
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
"""

update_comment = """
mutation UpdateComment(
  $commentId: ID!
  $content: String!
){
  updateComment(
    input: {
      id: $commentId
      contentMarkdown: $content
    }
  ){
    comment{
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
"""

remove_comment = """
mutation RemoveComment(
  $commentId: ID!
){
  removeComment(
    input: {
      id: $commentId
    }
  ){
    comment{
      id
    }
  }
}
"""

add_reply = """
mutation AddReply(
  $commentId: ID!
  $content: String!
){
  addReply(
    input: {
      commentId: $commentId
      contentMarkdown: $content
    }
  ){
    reply{
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
"""

update_reply = """
mutation UpdateReply(
  $commentId: ID!
  $content: String!
  $replyId: ID!
){
  updateReply(
    input: {
      commentId: $commentId
      contentMarkdown: $content
      replyId: $replyId
    }
  ){
    reply{
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
"""

remove_reply = """
mutation UpdateReply(
  $commentId: ID!
  $replyId: ID!
){
  removeReply(
    input: {
      commentId: $commentId
      replyId: $replyId
    }
  ){
    reply{
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
"""

publish_draft = """
mutation PublishDraft(
  $draftId: ObjectId!
){
  publishDraft(
    input: {
      draftId: $draftId
    }
  ){
    post{
      id
    }
  }
}
"""

schedule_draft = """
mutation RescheduleDraft(
  $draftId: ID!
  $publishAt: DateTime!
  $authorId: ID!
){
  scheduleDraft(
    input: {
      draftId: $draftId
      publishAt: $publishAt
      authorId: $authorId
    }
  ){
    scheduledPost{
      id
      author{username}
      draft{id}
      scheduledDate
      scheduledBy{username}
      publication{id}
    }
  }
}
"""

reschedule_draft = """
mutation RescheduleDraft(
  $draftId: ID!
  $publishAt: DateTime!
){
  rescheduleDraft(
    input: {
      draftId: $draftId
      publishAt: $publishAt
    }
  ){
    scheduledPost{
      id
      author{username}
      draft{id}
      scheduledDate
      scheduledBy{username}
      publication{id}
    }
  }
}
"""

cancel_schedule = """
mutation RescheduleDraft(
  $draftId: ID!
){
  cancelScheduledDraft(
    input: {
      draftId: $draftId
    }
  ){
    scheduledPost{
      id
    }
  }
}
"""

create_webhook = """
mutation Webhook(
  $publicationId: ID!
  $url: String!
  $events: [WebhookEvent!]!
  $secret: String!
){
  createWebhook(
    input: {
      publicationId: $publicationId
      url: $url
      events: $events
      secret: $secret
    }
  ){
    webhook{
      id
      url
      publication{id}
      events
      secret
      createdAt
      updatedAt
    }
  }
}
"""

update_webhook = """
mutation Webhook(
  $webhookId: ID!
  $url: String!
  $events: [WebhookEvent!]!
  $secret: String!
){
  updateWebhook(
    input: {
      id: $webhookId
      url: $url
      events: $events
      secret: $secret
    }
  ){
    webhook{
      id
      url
      publication{id}
      events
      secret
      createdAt
      updatedAt
    }
  }
}
"""

remove_webhook = """
mutation Webhook(
  $webhookId: ID!
){
  deleteWebhook(
      id: $webhookId
  ){
    webhook{
      id
    }
  }
}
"""