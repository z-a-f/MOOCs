require 'httparty'
require 'pp'
	
class Recipe
	include HTTParty

	base_uri		'http://food2fork.com/api'
	default_params	key: ENV['FOOD2FORK_KEY']
	format 			:json

	def self.for term
		#pp ENV
		get("/search", query: {q: term})['recipes']
	end
end
