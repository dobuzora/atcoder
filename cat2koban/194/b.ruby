n = gets
n = n.to_i
job_a = []
job_b = []

(1..n).each do
  ary = gets.split(" ")
  job_a.push ary[0].to_i
  job_b.push ary[1].to_i
end

job_a_min = job_a.min
job_a_index = job_a.index(job_a_min)
ans = job_a_min + job_b[job_a_index]

job_b[job_a_index] = ans
if job_b.min == ans
  puts ans
else
  neo_ans = [job_b.min, job_a.min]
  puts neo_ans.max
end
