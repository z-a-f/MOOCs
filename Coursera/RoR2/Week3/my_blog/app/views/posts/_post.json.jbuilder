#json.extract! post, :id, :title, :content, :created_at, :updated_at
json.extract! post, :title, :content, :created_at, :updated_at
json.url post_url(post, format: :json)