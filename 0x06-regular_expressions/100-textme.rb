#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:|to:|flags:)(?:\+?\d{11})?(?:\w+)?(?:[-\d:]*)?/).join(',')
