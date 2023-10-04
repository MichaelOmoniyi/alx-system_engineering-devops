#!/usr/bin/env ruby

# Check if the destination file argument is provided
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <DESTINATION_FILE>"
  exit 1
end

# Content of the template script
template_content = <<~RUBY
#!/usr/bin/env ruby
puts ARGV[0].scan(/REGEX HERE/).join
RUBY

# Get the destination file path from the command line argument
destination_file = ARGV[0]

# Write the template content to the specified destination file
File.open(destination_file, "w") do |file|
  file.puts(template_content)
end

puts "Template script copied to #{destination_file}"

# Open the destination file with vi
system("vi #{destination_file}")

