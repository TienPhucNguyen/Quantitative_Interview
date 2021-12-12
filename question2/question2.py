def exists(v,
          symbols=['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ/ς', 'τ', 'υ',
                   'φ',
                   'χ', 'ψ', 'ω']):
    return v in symbols

if exists('v'):
    print('v has been defined')
else:
    print("v hasn't been defined")
