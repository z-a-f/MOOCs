# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)


User.destroy_all

User.create! [
	{username: "Fiorina", password_digest: "1234"},
	{username: "Trump", password_digest: "1234"},
	{username: "Carson", password_digest: "1234"},
	{username: "Clinton", password_digest: "1234"},
]

usr = User.find_by!(username: "Fiorina")
	usr.create_profile!(
		gender: "female", 
		birth_year: 1954,
		first_name: "Carly",
		last_name: "Fiorina",
	)
	usr.todo_lists.create!(
		list_name: "Carly's List",
		list_due_date: Date.today + 1.year
	)
	usr.todo_lists.first.todo_items.create [
		{due_date: Date.today+1.year, title: "None", description: "None"},
		{due_date: Date.today+1.year, title: "None", description: "None"},
		{due_date: Date.today+1.year, title: "None", description: "None"},
		{due_date: Date.today+1.year, title: "None", description: "None"},
		{due_date: Date.today+1.year, title: "None", description: "None"},
	]

usr = User.find_by!(username: "Trump")
	usr.create_profile!(
		gender: "male", 
		birth_year: 1946,
		first_name: "Donald",
		last_name: "Trump",
	)
	usr.todo_lists.create!(
		list_name: "Donald's List",
		list_due_date: Date.today + 1.year
	)
	usr.todo_lists.first.todo_items.create [
		{due_date: Date.today+1.year, title: "None", description: "None"},
		{due_date: Date.today+1.year, title: "None", description: "None"},
		{due_date: Date.today+1.year, title: "None", description: "None"},
		{due_date: Date.today+1.year, title: "None", description: "None"},
		{due_date: Date.today+1.year, title: "None", description: "None"},
	]

usr = User.find_by!(username: "Carson")
	usr.create_profile!(
		gender: "male", 
		birth_year: 1951,
		first_name: "Ben",
		last_name: "Carson",
	)
	usr.todo_lists.create!(
		list_name: "Ben's List",
		list_due_date: Date.today + 1.year
	)
	usr.todo_lists.first.todo_items.create [
		{due_date: Date.today+1.year, title: "None", description: "None"},
		{due_date: Date.today+1.year, title: "None", description: "None"},
		{due_date: Date.today+1.year, title: "None", description: "None"},
		{due_date: Date.today+1.year, title: "None", description: "None"},
		{due_date: Date.today+1.year, title: "None", description: "None"},
	]

usr = User.find_by!(username: "Clinton")
	usr.create_profile!(
		gender: "female", 
		birth_year: 1947,
		first_name: "Hillary",
		last_name: "Clinton",
	)
	usr.todo_lists.create!(
		list_name: "Hillary's List",
		list_due_date: Date.today + 1.year
	)
	usr.todo_lists.first.todo_items.create [
		{due_date: Date.today+1.year, title: "None", description: "None"},
		{due_date: Date.today+1.year, title: "None", description: "None"},
		{due_date: Date.today+1.year, title: "None", description: "None"},
		{due_date: Date.today+1.year, title: "None", description: "None"},
		{due_date: Date.today+1.year, title: "None", description: "None"},
	]

