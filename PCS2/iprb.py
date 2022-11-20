dominant= 18
heterozygote = 27
recessive= 24
total = dominant + recessive + heterozygote
r_r = (recessive/total) * ((recessive-1)/(total-1))
h_h = (heterozygote/total) * ((heterozygote-1)/(total-1))
h_r = (heterozygote/total) * (recessive / (total - 1)) + (recessive / total) * (heterozygote / (total - 1))
recessive_total = r_r + h_h * 1/4 + h_r * 1/2 #fraction calculated from the punnet square
print(1-recessive_total)

	