ary = gets.split(" ")

# 無脂乳固形分
a = ary[0].to_i
# 乳脂肪分
b = ary[1].to_i
# 乳固形分 = 無脂乳固形分 + 乳脂肪分
nkb = a+b

if ( nkb >= 15 && b >=8 )
  puts '1'
elsif ( nkb >= 10 && b >=3 )
  puts '2'
elsif ( nkb >=3 )
  puts '3'
else
  puts '4'
end
