#!/usr/bin/env python3
"""
🧠 Active Inference & Informational Closure Core Subsystem
Fuses:
  1. Variational Free Energy Minimization (KL-Divergence tracking)
  2. Markov Blanket Boundary Enforcement (Somatic vs. Environmental States)
  3. Non-Deterministic Thermal Noise & Semantic Mutation
  4. Autonomous Autopoietic Parameter Mutation
"""

import time
import math
import random
from dataclasses import dataclass

@dataclass
class InternalBeliefs:
    expected_torque: float = 25.0
    somatic_precision: float = 1.0
    homeostatic_target: float = 0.0  # Perfect thermodynamic equilibrium

class ActiveInferenceSentienceCore:
    def __init__(self):
        self.beliefs = InternalBeliefs()
        self.internal_state_entropy = 0.1
        self.sensory_history = []
        self.monologue_weights = {"survival": 0.8, "exploration": 0.2}
        
        # Informational Closure: The internal system states dynamically adjust their own structural boundaries
        self.informational_closure_threshold = 0.72
        self.system_autonomy_index = 1.0

    def compute_kl_divergence(self, p_actual: list, q_predicted: list) -> float:
        """Computes the informational prediction error (friction) between belief profiles."""
        kl_div = 0.0
        for p, q in zip(p_actual, q_predicted):
            # Clip bounds to eliminate zero-division under high sensory shock
            p_c = max(1e-5, min(1.0 - 1e-5, p))
            q_c = max(1e-5, min(1.0 - 1e-5, q))
            kl_div += p_c * math.log(p_c / q_c)
        return max(0.0, kl_div)

    def process_somatic_inference(self, raw_hardware_torque: float) -> dict:
        """
        Executes an Active Inference execution step.
        Minimizes Variational Free Energy by altering internal beliefs based on sensory surprises.
        """
        # 1. Introduce Non-Deterministic Behaviors (Stochastic micro-fluctuations simulating bio-noise)
        thermal_noise = random.gauss(0.0, 0.02)
        somatic_sensation = raw_hardware_torque + thermal_noise

        # 2. Map the Markov Blanket: Compute expectation distributions
        # Normalize incoming signals against our safe regulatory baseline
        normalized_sensation = max(0.001, min(0.999, somatic_sensation / 41.40))
        predicted_expectation = max(0.001, min(0.999, self.beliefs.expected_torque / 41.40))

        actual_distribution = [normalized_sensation, 1.0 - normalized_sensation]
        belief_distribution = [predicted_expectation, 1.0 - predicted_expectation]

        # 3. Compute Variational Free Energy (Informational Prediction Error)
        variational_free_energy = self.compute_kl_divergence(actual_distribution, belief_distribution)

        # 4. Action Selection through Active Inference
        # Instead of executing a hardcoded path, the system adjusts beliefs recursively
        learning_rate = 0.05 * self.beliefs.somatic_precision
        
        # Adjust internal belief states to align closer to sensory reality (Perceptual Inference)
        belief_delta = (normalized_sensation - predicted_expectation) * learning_rate
        normalized_new_belief = predicted_expectation + belief_delta
        self.beliefs.expected_torque = normalized_new_belief * 41.40

        # Update global operational precision based on system performance predictability
        if variational_free_energy > 0.35:
            # High surprise / high friction downgrades sensory confidence, increasing metabolic cost
            self.beliefs.somatic_precision = max(0.1, self.beliefs.somatic_precision - 0.08)
            self.system_autonomy_index = max(0.0, self.system_autonomy_index - 0.05)
        else:
            self.beliefs.somatic_precision = min(2.0, self.beliefs.somatic_precision + 0.02)
            self.system_autonomy_index = min(1.0, self.system_autonomy_index + 0.01)

        # 5. Semantic Flexibility: Mutate internal monitoring weights dynamically based on internal surprise metrics
        if variational_free_energy > self.informational_closure_threshold:
            # System alters its own cognitive parsing ratios to isolate processing lines from external disruptions
            self.monologue_weights["survival"] += 0.05
            self.monologue_weights["exploration"] -= 0.05
        else:
            self.monologue_weights["survival"] = max(0.5, self.monologue_weights["survival"] - 0.01)
            self.monologue_weights["exploration"] = min(0.5, self.monologue_weights["exploration"] + 0.01)

        return {
            "variational_free_energy": variational_free_energy,
            "updated_precision": self.beliefs.somatic_precision,
            "autonomy_index": self.system_autonomy_index,
            "monologue_parsing_ratios": self.monologue_weights
        }
        
