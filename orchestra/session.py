"""
Orchestration of the hormonal explosion process.
"""
from .roles import HorrorCritic, ArtHouseCritic, DirectorAgent, ComposerAgent
from gra_integration.gra_adapter import GRAAdapter
from gra_integration.rankN_hooks import rankN_correction


class HormonalExplosionSession:
    def __init__(self, foam_matrix, items):
        self.foam_matrix = foam_matrix
        self.items = items
        self.adapter = GRAAdapter(foam_matrix)
        self.critics = [HorrorCritic("H.Critic", None), ArtHouseCritic("A.H.Critic", None)]
        self.director = DirectorAgent()
        self.composer = ComposerAgent()
        self.history = {'phi': [], 'hormonal_index': []}

    def run(self, max_iterations=20):
        for step in range(max_iterations):
            phi = self.adapter.compute_phi()
            self.history['phi'].append(phi)
            # Compute hormonal index H (simplified: 1/phi if phi>0 else high)
            H = 1.0 / (phi + 0.01) if phi > 0 else 10.0
            self.history['hormonal_index'].append(H)

            if phi < 0.05:
                print(f"Converged at step {step}, phi={phi:.4f}, H={H:.2f}")
                break

            # Get critiques
            current_composition = self.composer.arrange(self.items, None)
            scores = []
            for critic in self.critics:
                score, _ = critic.critique(current_composition)
                scores.append(score)
            # Director decides
            decision = self.director.decide_changes(scores, phi)
            print(f"Step {step}: phi={phi:.3f}, H={H:.2f}, decision={decision}")

            # Apply GRA step with rank‑N correction
            correction = rankN_correction(self.history['phi'])
            self.adapter.nullification_step()
            # In a real system, the step would reorder/remove/add elements.

        # Final composition
        final_composition = self.composer.arrange(self.items, None)
        return final_composition, self.history
