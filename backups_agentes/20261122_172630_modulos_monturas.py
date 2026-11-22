class PersonajeProgresion:
    # ... (código existente)
    
    def obtener_stats_reales(self, bono_montura: dict = None):
        """
        Calcula las estadísticas finales sumando las base + bonos.
        bono_montura: {'stat': 'VIT', 'valor': 5}
        """
        stats_finales = self.stats.copy()
        if bono_montura and bono_montura["stat"] in stats_finales:
            stats_finales[bono_montura["stat"]] += bono_montura["valor"]
        
        return stats_finales
