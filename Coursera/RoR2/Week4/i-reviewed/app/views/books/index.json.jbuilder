json.array!(@books) do |book|
  json.extract! book, :id, :name, :author
  json.url book_url(book, format: :json)
end
