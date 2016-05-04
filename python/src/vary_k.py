#
# AUTO-GENERATED FILE. DO NOT EDIT
# CodeBuff 1.4.3 'Tue May 03 23:35:42 PDT 2016'
#
import numpy as np
import matplotlib.pyplot as plt

java=[0.07020408, 0.061068702, 0.05498982, 0.050884955, 0.051502146, 0.05263158, 0.050946143, 0.050643776, 0.04978541, 0.050643776, 0.050643776, 0.046902657, 0.046902657, 0.050111357, 0.050111357, 0.050884955, 0.049358647]
java8=[0.06306554, 0.048702635, 0.04301746, 0.042372882, 0.040089086, 0.037383176, 0.039473683, 0.03830313, 0.0389755, 0.037861917, 0.0389755, 0.037861917, 0.037861917, 0.0389755, 0.0389755, 0.037861917, 0.043613706]
antlr=[0.2752809, 0.2547945, 0.25585106, 0.2547945, 0.25477707, 0.23424658, 0.23424658, 0.23424658, 0.23731138, 0.22554348, 0.22154373, 0.22554348, 0.22554348, 0.22554348, 0.22554348, 0.22535461, 0.218401]
sqlite=[0.114035085, 0.107279696, 0.10526316, 0.09881423, 0.097058825, 0.097058825, 0.091121495, 0.09536785, 0.093457945, 0.09375, 0.096491225, 0.09539474, 0.09798995, 0.09881423, 0.09798995, 0.09881423, 0.100286536]
tsql=[0.1124031, 0.09834191, 0.09443099, 0.08805031, 0.09500805, 0.08571429, 0.08888889, 0.08027523, 0.08089501, 0.081001475, 0.082474224, 0.08495145, 0.08146873, 0.08394698, 0.086892486, 0.086892486, 0.07788162]

ks = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 131]
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(ks, java, label="java", marker='o')
ax.plot(ks, java8, label="java8", marker='o')
ax.plot(ks, antlr, label="antlr", marker='o')
ax.plot(ks, sqlite, label="sqlite", marker='o')
ax.plot(ks, tsql, label="tsql", marker='o')
ax.set_xlabel("k nearest neighbors")
ax.set_ylabel("Error rate")
ax.set_title("k Nearest Neighbors vs\nLeave-one-out Validation Error Rate")
plt.legend()
fig.savefig('images/vary_k.pdf', format='pdf')
plt.show()