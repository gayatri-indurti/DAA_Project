class StableMatch:
def __init__(self, count) -> None:
self.n = count

def get_grps(self, group1, group2):
self.A_B = [group1, group2]

def get_preference_grp1(self, grp1):
self.A = grp1

def get_preference_grp2(self, grp2):
self.B = grp2

def select_proposing_group(self, value):
if (value == 1):
self.proposing_group = 0
self.proposed_group = 1

def create_unmatched_list(self):
self.unmatched = []
for i in self.A_B[self.proposing_group]:
self.unmatched.append(i)

def create_current_partner_matrix(self):
self.current_partners = [[], []]
for i in range(self.n):
self.current_partners[0].append('_')
self.current_partners[1].append('_')

def create_proposed_matrix(self):
self.proposed = []
for i in range(self.n):
var = []
for j in range(self.n):
var.append(0)
self.proposed.append(var)
def calculate_stable_match(self):
while (len(self.unmatched) > 0):
current_male = self.unmatched.pop(0)
i = self.A_B[self.proposing_group].index(current_male)
for j in range(self.n):
if self.proposed[i][j] == 0:
self.proposed[i][j] = 1
current_female = self.A[i][j]
male_index =

self.A_B[self.proposing_group].index(current_male)

female_index =

self.A_B[self.proposed_group].index(current_female)
if current_female in self.current_partners[

self.proposed_group]: defending_male =

self.current_partners[self.proposing_group][

self.current_partners[self.proposed_group].index(current_female)]
defending_male_pos = self.B[female_index].index(defending_male)

current_male_pos =
self.B[female_index].index(current_male)

if current_male_pos < defending_male_pos:

self.current_partners[self.proposing_group][

self.A_B[self.proposing_group].index(defending_male)] = '_'
self.current_partners[self.proposed_group][

self.A_B[self.proposing_group].index(defending_male)] = '_'
self.current_partners[self.proposing_group][
self.A_B[self.proposing_group].index(current_male)]

= current_male

self.current_partners[self.proposed_group][
self.A_B[self.proposing_group].index(current_male)]

= current_female

self.unmatched.insert(self.proposing_group,

defending_male)
break
else:
self.current_partners[self.proposing_group][male_index] =

current_male

self.current_partners[self.proposed_group][male_index] =

current_female
break

return self.current_partners
