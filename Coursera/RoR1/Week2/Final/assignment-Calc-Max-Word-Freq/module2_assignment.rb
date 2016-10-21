#Implement all parts of this assignment within (this) module2_assignment2.rb file

#Implement a class called LineAnalyzer.
class LineAnalyzer
  #Implement the following read-only attributes in the LineAnalyzer class. 
  #* highest_wf_count - a number with maximum number of occurrences for a single word (calculated)
  #* highest_wf_words - an array of words with the maximum number of occurrences (calculated)
  #* content          - the string analyzed (provided)
  #* line_number      - the line number analyzed (provided)
  attr_reader	:highest_wf_count, :highest_wf_words, :content, :line_number

  #* initialize() - taking a line of text (content) and a line number
  def initialize(line, line_number)
    #Implement the initialize() method to:
    #* take in a line of text and line number
    #* initialize the content and line_number attributes
    #* call the calculate_word_frequency() method.
    @content = line
    @line_number = line_number
    calculate_word_frequency()
  end

  #* calculate_word_frequency() - calculates result
  def calculate_word_frequency()
    #Implement the calculate_word_frequency() method to:
    #* calculate the maximum number of times a single word appears within
    #  provided content and store that in the highest_wf_count attribute.
    #* identify the words that were used the maximum number of times and
    #  store that in the highest_wf_words attribute.
    word_hash = Hash.new(0)
    @content.split.each do |word|
      word_hash[word.downcase] += 1
    end

    @highest_wf_count = word_hash.max_by { |word, freq| freq }[1]
    @highest_wf_words = word_hash.select { |word, freq| freq == @highest_wf_count }.keys
    # p word_hash
    # p @highest_wf_count
    # p @highest_wf_words
    
  end
end

#  Implement a class called Solution. 
class Solution

  # Implement the following read-only attributes in the Solution class.
  #* analyzers - an array of LineAnalyzer objects for each line in the file
  #* highest_count_across_lines - a number with the maximum value for highest_wf_words attribute in the analyzers array.
  #* highest_count_words_across_lines - a filtered array of LineAnalyzer objects with the highest_wf_words attribute 
  #  equal to the highest_count_across_lines determined previously.
  attr_reader	:analyzers, :highest_count_across_lines, :highest_count_words_across_lines

  def initialize
    @analyzers = []
  end
  
  # Implement the following methods in the Solution class.
  
  #* analyze_file() - processes 'test.txt' intro an array of LineAnalyzers and stores them in analyzers.
  def analyze_file()
    # Implement the analyze_file() method() to:
    #* Read the 'test.txt' file in lines 
    #* Create an array of LineAnalyzers for each line in the file
    if File.exist? 'test.txt'
      idx = 0
      File.foreach('test.txt') do |line|
        @analyzers.push LineAnalyzer.new(line, idx)
        idx += 1
        
      end
    end
  end

  #* calculate_line_with_highest_frequency() - determines the highest_count_across_lines and 
  #  highest_count_words_across_lines attribute values
  def calculate_line_with_highest_frequency()
    # Implement the calculate_line_with_highest_frequency() method to:
    #* calculate the maximum value for highest_wf_count contained by the LineAnalyzer objects in analyzers array
    #  and stores this result in the highest_count_across_lines attribute.
    #* identifies the LineAnalyzer objects in the analyzers array that have highest_wf_count equal to highest_count_across_lines 
    #  attribute value determined previously and stores them in highest_count_words_across_lines.
    @highest_count_across_lines = @analyzers.max_by { |analyzer| analyzer.highest_wf_count }.highest_wf_count
    @highest_count_words_across_lines = @analyzers.select { |analyzer| analyzer.highest_wf_count == @highest_count_across_lines }
    #p @highest_count_across_lines
    #p @highest_count_words_across_lines
  end
  
  #* print_highest_word_frequency_across_lines() - prints the values of LineAnalyzer objects in 
  #  highest_count_words_across_lines in the specified format
  def print_highest_word_frequency_across_lines()
    #Implement the print_highest_word_frequency_across_lines() method to
    #* print the values of objects in highest_count_words_across_lines in the specified format
    @highest_count_words_across_lines.each do |analyzer|
      puts "#{analyzer.highest_wf_words} (appears in line #{analyzer.line_number})"
    end
  end
  
end
