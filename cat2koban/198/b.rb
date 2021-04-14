s = gets.to_i

if s == 0
  puts "Yes"
  return
end

while (s%10==0) do s /= 10 end
puts s.to_s == s.to_s.reverse ? "Yes" : "No"
