import kenlm

model = kenlm.Model('trained_models/kenlm_8_without_padding.arpa')
print(model.score("msg canvas pack msg <unk>"))