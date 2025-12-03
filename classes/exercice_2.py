class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError
        self._celsius = value
        
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    

def main():
    temp = Temperature(25)
    print(temp.celsius)     
    print(temp.fahrenheit)  
    temp.celsius = -100 
        

if __name__ == "__main__":
    main()   








# ### **🟡 Exercice 2 : `@property` et Validation**

# Créez une classe `Temperature` avec :
# - Attribut privé `_celsius`
# - Property `celsius` avec getter et setter
# - Le setter doit rejeter les températures < -273.15 (zéro absolu)
# - Property `fahrenheit` (lecture seule) qui convertit : `F = C * 9/5 + 32`
# ```python
# # Votre code ici

# # Test
# temp = Temperature(25)
# print(temp.celsius)     # 25
# print(temp.fahrenheit)  # 77.0
# temp.celsius = -300     # ValueError!



# ## 📊 **Diagramme du flow**
# ```
# Utilisateur fait : temp.celsius = 25
#                     ↓
#             Appelle le SETTER
#                     ↓
#         Validation : 25 > -273.15 ? ✅
#                     ↓
#         Stockage dans _celsius = 25
#                     ↓
#             Succès !

# ---

# Utilisateur fait : print(temp.celsius)
#                     ↓
#             Appelle le GETTER
#                     ↓
#         Retourne self._celsius (25)
#                     ↓
#             Affiche 25

# ---

# Utilisateur fait : print(temp.fahrenheit)
#                     ↓
#             Appelle le GETTER fahrenheit
#                     ↓
#         Calcule : 25 * 9/5 + 32 = 77.0
#                     ↓
#             Affiche 77.0