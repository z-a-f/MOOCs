class AddUserRefToTodoList < ActiveRecord::Migration
  def change
  	add_reference :todo_lists, :user, index: true, foreign_key: true
  end
end
