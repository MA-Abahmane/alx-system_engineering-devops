#!/usr/bin/env ruby

# For this task, I’ll be taking over Guillaume’s responsibilities: one afternoon,
#   a TextMe VoIP Engineer comes to you and explains she wants to run some statistics
#     on the TextMe app text messages transactions.

# USAGE: ./100-textme.rb [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1]
# My script will output: [SENDER (from)],[RECEIVER (to)],[FLAGS]

# get the data in front of the titles 'from', 'to' and 'flags'
txt_from = ARGV[0].scan(/from:([^\[\]]+)/).flatten
txt_to = ARGV[0].scan(/to:([^\[\]]+)/).flatten
txt_flags = ARGV[0].scan(/flags:([^\[\]]+)/).flatten

# joint the matched srings with ',' spliting them
rez = [txt_from, txt_to, txt_flags].join(',')

# print the resulte
puts rez
