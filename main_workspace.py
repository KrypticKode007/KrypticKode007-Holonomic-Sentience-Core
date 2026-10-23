#!/usr/bin/env python3
import time
import threading
from dataclasses import dataclass
from modules.branch_01_homeostatic import HomeostaticEngine
from modules.branch_02_autonoetic import AutonoeticWorkspace
from modules.branch_03_metacognitive import MetacognitiveEvaluator
from modules.branch_04_crypto_vault import CryptoVault
from modules.branch_05_telemetry import TelemetryMonitor
from modules.branch_06_swarm_mesh import SwarmMeshBus
from modules.branch_07_api_metrics import PrometheusMetricsAPI
from modules.branch_08_blueprint import BlueprintCompiler
from modules.branch_09_action_node import ActionNode
from modules.branch_10_kalman_filter import BayesianKalmanFilter

@dataclass
class SharedState:
    valence: float = 1.0
    arousal: float = 0.5
    anxiety: float = 0.0
    exhaustion: float = 0.0
    integrity: float = 1.0
    hope_level: float = 1.0  # Maintained boundary constraint
    
    # New Active Inference tracking metrics
    variational_free_energy: float = 0.0
    somatic_precision: float = 1.0
    is_conscious: str = "CONSCIOUS"
    is_running: bool = True


def main():
    state = SharedState()
    print("🚀 Initializing all 10 branches of the cybernetic sentience engine...")

    # Instantiate modules
    vault = CryptoVault()
    homeostatic = HomeostaticEngine(state)
    autonoetic = AutonoeticWorkspace(state)
    meta = MetacognitiveEvaluator(state, vault)
    telemetry = TelemetryMonitor(state)
    mesh = SwarmMeshBus()
    api = PrometheusMetricsAPI(state)
    compiler = BlueprintCompiler(state)
    action = ActionNode(state)
    kalman = BayesianKalmanFilter()

    # Start API and Swarm network listeners
    threading.Thread(target=api.start, daemon=True).start()
    threading.Thread(target=mesh.start_receiver, daemon=True).start()

    print("⚡ System running. Press Ctrl+C to wind down engine loops safely.")

while state.is_running:
    # Step 1: Poll physical hardware metrics
    raw_torque = telemetry.poll_hardware()

    # Step 2: Feed raw metrics directly into the Active Inference engine
    # This automatically runs the neuromorphic Kalman filter, updates beliefs,
    # and handles episodic database consolidation spikes under high entropy
    homeostatic.process_active_inference_cycle(raw_torque)

    # Step 3: Map the recalculated engine metrics back to the shared state bus
    state.valence = homeostatic.state.valence
    state.exhaustion = homeostatic.state.exhaustion
    state.variational_free_energy = homeostatic.compute_kl_divergence(
        [max(0.001, min(0.999, homeostatic.kalman_estimate / 41.40)), 1.0 - max(0.001, min(0.999, homeostatic.kalman_estimate / 41.40))],
        [max(0.001, min(0.999, homeostatic.beliefs.expected_torque / 41.40)), 1.0 - max(0.001, min(0.999, homeostatic.beliefs.expected_torque / 41.40))]
    )
    state.somatic_precision = homeostatic.beliefs.somatic_precision

    # Step 4: Continue downstream execution paths (API presentation, narratives, etc.)
    narrative = autonoetic.generate_manifest(state.variational_free_energy)
    compiler.export_blueprint()

    time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("\n🛑 Terminating engine loops...")
        state.is_running = False
        api.stop()
        mesh.stop()
        print("💤 Engine closed cleanly.")

if __name__ == "__main__":
    main()
