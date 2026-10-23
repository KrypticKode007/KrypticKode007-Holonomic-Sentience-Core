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
    try:
        while state.is_running:
            # Step 1: Read Telemetry and Smooth via Bayesian Kalman Pipeline
            raw_telemetry = telemetry.poll_hardware()
            smoothed_input = kalman.filter_step(raw_telemetry)

            # Step 2: Update Homeostatic State & Action Execution
            homeostatic.update_loop(smoothed_input)
            action.execute_tick()

            # Step 3: Compile State Narrative Manifests
            narrative = autonoetic.generate_manifest(smoothed_input)
            meta.evaluate_friction(narrative)

            # Step 4: Write Blueprint Status Alerts
            compiler.export_blueprint()

            # Rapid cycle loop throttle
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n🛑 Terminating engine loops...")
        state.is_running = False
        api.stop()
        mesh.stop()
        print("💤 Engine closed cleanly.")

if __name__ == "__main__":
    main()
