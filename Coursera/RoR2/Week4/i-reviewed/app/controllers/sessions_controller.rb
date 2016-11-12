class SessionsController < ApplicationController
  skip_before_action :ensure_login, only: [:new, :create]
  def new
  	# Login Page - new.html.erb
  end

  def create
  	reviewer = Reviewer.find_by(name: params[:reviewer][:name])
  	password = params[:reviewer][:password]

  	if reviewer && reviewer.authenticate(password)
  	  session[:reviewer_id] = reviewer.id
  	  redirect_to root_path, notice: "Logged in successfully"
  	else
  	  redirect_to login_path, alert: "Invalid username/password combination"
  	end
  end

  def destroy
  	reset_session # wipe out session and everything in it
    redirect_to login_path, notice: "You have been logged out"
  end
end


