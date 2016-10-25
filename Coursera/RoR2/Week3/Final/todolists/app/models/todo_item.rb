class TodoItem < ActiveRecord::Base
	def self.count_completed
		self.where(completed: true).count
	end
end
