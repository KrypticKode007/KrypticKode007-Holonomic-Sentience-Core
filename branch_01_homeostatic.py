#!/usr/bin/env python3
"""
🧠 Active Inference, Neuromorphic Smoothing, and Episodic Integration Core
Repository Integration: KrypticKode007/kryptic-agent (2026 Framework)

Fuses:
  1. Variational Free Energy Minimization (KL-Divergence Tracking)
  2. Neuromorphic Kalman Filtering (Dynamic Precision Noise Scaling)
  3. Automated Episodic Ledger Spiking & Memory Consolidation Loops
"""

import os
import sys
import time
import math
import random
import sqlite3
import gzip
import shutil
from dataclasses import dataclass

@dataclass
class InternalBeliefs:
    expected_torque: float = 25.0
    somatic_precision: float = 1.0
    homeostatic_target: float = 0.0

@dataclass
class CognitiveState:
    valence: float
    arousal: float
    anxiety: float
    exhaustion: float
    system_integrity: float


class ActiveInferenceHomeostaticEngine:
    def __init__(self, node_id="KrypticCore_Sentience", db_path="sentience_core_ledger.db"):
        self.node_id = node_id
        self.db_path = db_path
        self.archive_dir = "archived_memories"
        
        # State initializations
        self.beliefs = InternalBeliefs()
        self.state = CognitiveState(1.0, 0.5, 0.0, 0.0, 1.0)
        self.monologue_weights = {"survival": 0.8, "exploration": 0.2}
        
        # Free Energy thresholds and boundaries
        self.informational_closure_threshold = 0.72
        self.consolidation_trigger_spike = 0.85
        self.in_sleep_cycle = False
        
        # Kalman filter properties (Neuromorphic properties scale base noise values)
        self.kalman_estimate = 25.0
        self.kalman_error_cov = 1.0
        self.base_process_noise = 0.01
        self.base_measurement_noise = 0.1  # Shifted dynamically by somatic precision
        
        os.makedirs(self.archive_dir, exist_ok=True)
        self._initialize_vault()

    def _initialize_vault(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS episodic_vault (
                    timestamp REAL,
                    node_id TEXT,
                    free_energy REAL,
                    precision REAL,
                    exhaustion REAL,
                    somatic_sensation REAL
                )
            """)
            conn.commit()

    def compute_kl_divergence(self, p_actual: list, q_predicted: list) -> float:
        kl_div = 0.0
        for p, q in zip(p_actual, q_predicted):
            p_c = max(1e-5, min(1.0 - 1e-5, p))
            q_c = max(1e-5, min(1.0 - 1e-5, q))
            kl_div += p_c * math.log(p_c / q_c)
        return max(0.0, kl_div)

    def neuromorphic_kalman_filter(self, raw_measurement: float) -> float:
        """Scales measurement noise inversely against sensory validation confidence metrics."""
        # High precision confidence compresses raw sensor error margins on the fly
        dynamic_measurement_noise = self.base_measurement_noise / max(1e-3, self.beliefs.somatic_precision)
        
        # Predict phase
        self.kalman_error_cov += self.base_process_noise
        
        # Update phase
        kalman_gain = self.kalman_error_cov / (self.kalman_error_cov + dynamic_measurement_noise)
        self.kalman_estimate += kalman_gain * (raw_measurement - self.kalman_estimate)
        self.kalman_error_cov *= (1.0 - kalman_gain)
        
        return self.kalman_estimate

    def process_active_inference_cycle(self, raw_torque: float):
        """Orchestrates the active sensory analysis, free energy checks, and memory spikes."""
        # 1. Inject stochastic structural variance (Non-deterministic hardware simulation)
        thermal_noise = random.gauss(0.0, 0.02)
        noisy_sensation = raw_torque + thermal_noise
        
        # 2. Smooth signal using neuromorphic Kalman tracking rules
        smoothed_sensation = self.neuromorphic_kalman_filter(noisy_sensation)
        
        # 3. Formulate normalized belief/sensory comparison frames
        normalized_sensation = max(0.001, min(0.999, smoothed_sensation / 41.40))
        predicted_expectation = max(0.001, min(0.999, self.beliefs.expected_torque / 41.40))
        
        actual_dist = [normalized_sensation, 1.0 - normalized_sensation]
        belief_dist = [predicted_expectation, 1.0 - predicted_expectation]
        
        # 4. Extract Variational Free Energy
        free_energy = self.compute_kl_divergence(actual_dist, belief_dist)
        
        # 5. Adapt perceptual learning values based on outcome surprise indices
        learning_rate = 0.05 * self.beliefs.somatic_precision
        self.beliefs.expected_torque += (smoothed_sensation - self.beliefs.expected_torque) * learning_rate
        
        # 6. Apply Semantic Flexibility adjustments
        if free_energy > self.informational_closure_threshold:
            self.beliefs.somatic_precision = max(0.1, self.beliefs.somatic_precision - 0.08)
            self.monologue_weights["survival"] = min(1.0, self.monologue_weights["survival"] + 0.05)
            self.monologue_weights["exploration"] = max(0.0, self.monologue_weights["exploration"] - 0.05)
        else:
            self.beliefs.somatic_precision = min(2.0, self.beliefs.somatic_precision + 0.02)
            
        # Increment operational wear profile
        self.state.exhaustion += 0.002
        
        # 7. Automated Episodic Ledger Storage & Validation Spikes
        self._log_transaction(free_energy, smoothed_sensation)
        
        if free_energy > self.consolidation_trigger_spike or self.state.exhaustion > 0.8:
            self.trigger_sleep_consolidation()

    def _log_transaction(self, free_energy: float, sensation: float):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO episodic_vault (timestamp, node_id, free_energy, precision, exhaustion, somatic_sensation)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (time.time(), self.node_id, free_energy, self.beliefs.somatic_precision, self.state.exhaustion, sensation))
            conn.commit()

    def trigger_sleep_consolidation(self):
        if self.in_sleep_cycle:
            return
        self.in_sleep_cycle = True
        print(f"💤 Free energy anomaly or high cognitive exhaustion detected. Engaging memory compaction...")
        try:
            archive_file = os.path.join(self.archive_dir, f"inf_closure_backup_{int(time.time())}.db.gz")
            with open(self.db_path, 'rb') as f_in:
                with gzip.open(archive_file, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            self.state.exhaustion = 0.0  # Reset load following consolidation completion
        except Exception:
            pass
        finally:
            self.in_sleep_cycle = False


if __name__ == "__main__":
    print("Testing active inference homeostatic iteration loop...")
    engine = ActiveInferenceHomeostaticEngine()
    # Simulate a series of sensory telemetry ticks with a sudden high-torque perturbation
    for tick in range(15):
        simulated_torque = 43.5 if tick == 8 else 24.0
        engine.process_active_inference_cycle(simulated_torque)
        time.sleep(0.05)
      
