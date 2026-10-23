# Inside your master main() execution loop:
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
  
