# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)
Book.destroy_all
Reviewer.destroy_all


Book.create! [
	{name: "Eloquent Ruby", author: "Russ Olsen"},
	{name: "Beginning Ruby", author: "Peter Cooper"},
	{name: "Metaprogramming Ruby 2", author: "Paolo Perotta"},
	{name: "Design Patterns in Ruby", author: "Russ Olsen"},
	{name: "The Ruby Programming Language", author: "David Flanagan"}
]

100.times { |index| Book.create! name: "Book#{index}", author: "Author#{index}"}

eloquent = Book.find_by name: "Eloquent Ruby"
eloquent.notes.create! [
	{title: "Wow!", note: "Great book to learn Ruby!"},
	{title: "Meh", note: "It's an OK book." }
]

reviewers = Reviewer.create! [
  { name: "Joe", password: "abc123" },
  { name: "Jim", password: "123abc" },
  { name: "Zafar", password: "password"}
]

Book.all.each do |book|
  book.reviewer = reviewers.sample
  book.save!
end
