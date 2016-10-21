## What is this?

This repo is a small, but working POC (Proof of Concept) of how we might accomplish ["Blackbox testing"](https://en.wikipedia.org/wiki/Black-box_testing)

## Watch the video about Blackbox Testing that uses this repo

https://www.coursera.org/learn/ruby-on-rails-intro/lecture/RbJIe/blackbox-testing

## How do we blackbox-test a webapp (Rails or any webapp really) using Ruby? (And why should we use Ruby for this?)

Enter [RSpec](https://relishapp.com/rspec/docs/gettingstarted) + [Capybara](https://github.com/jnicklas/capybara) ruby gems. When these 2 frameworks come together, you can write very intuitive and expressive tests. 

For example, can you tell what the following test does?

```ruby
describe "Recipes App" do
  it "displays chocolate by default" do
    visit "/"
    expect(page).to have_content 'Chocolate Tea'
  end

  it "displays beef when keyword is beef" do
    visit "?keyword=beef"
    expect(page).to have_content 'Delicious Scalloped Potato'  	
  end
end
```  

##How do I get started?

1. Install PhantomJS (http://phantomjs.org/)
2. Run the following inside your terminal:

  ```shell
  $ gem install rspec
  $ gem install selenium-webdriver
  $ gem install capybara
  $ gem install poltergeist
  ```
2. (If you are using `rbenv`, also run `$rbenv rehash`)  
3. Pull down this repo
4. Run the following in your terminal (right outside of `spec` dir):

   ```shell
   $ rspec
   ```

   or even better

   ```shell
   $ rspec -f d
   ```

   to see the magic.

## Headless mode

```ruby
# Capybara.default_driver = :selenium
# Headless
Capybara.default_driver = :poltergeist
```
