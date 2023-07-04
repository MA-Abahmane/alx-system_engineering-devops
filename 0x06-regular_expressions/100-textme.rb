#!/usr/bin/env ruby

txt_from = ARGV[0].scan(/from:([^]]+)/).flatten
txt_to = ARGV[0].scan(/to:([^]]+)/).flatten
txt_flags = ARGV[0].scan(/flags:([^]]+)/).flatten

rez = [txt_from, txt_to, txt_flags].joint(',')
puts rez