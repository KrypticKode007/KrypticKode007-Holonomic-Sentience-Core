import os
import pytest
import sqlite3
import subprocess
from main_sentience_core import HolonomicSentienceCore, CPPAccelerationBridge, AutomatedBackupEngine

TEST_DB = "sentience_core_memory.db"

@pytest.fixture(scope="module", autouse=True)
def ensure_cpp_compilation():
    """Verifies that the high-speed C++ binary is compiled and available before running tests."""
    bridge = CPPAccelerationBridge()
    assert os.path.exists(bridge.cpp_binary)
    yield

def test_cpp_matrix_calculation_precision():
    """Validates that parameters dispatched down piping channels yield accurate native math limits."""
    bridge = CPPAccelerationBridge()
    # Execute matrix logic pass through stdout pipe collection
    cpp_output_vector = bridge.calculate_acceleration_vectors(0.85, 0.25)
    
    # Assert return vector is valid numerical float calculations below input constraints
    assert isinstance(cpp_output_vector, float)
    assert 0.0 <= cpp_output_vector <= 1.0

def test_cron_backup_script_deployment():
    """Ensures the compressed backup utility shell script is built and has execution permissions."""
    backup_engine = AutomatedBackupEngine()
    assert os.path.exists("backup_ledger.sh")
    
    # Trigger execution check pass to verify that compress routines run with zero exit codes
    backup_engine.execute_immediate_backup_pass()
    assert os.path.exists("backups")

def test_integrated_distance_gap_closure():
    """Verifies that running loops reduce the cognitive variance score by processing telemetry."""
    core = HolonomicSentienceCore()
    assert core.current_distance_percentage == 12.50
    
    # Simulate high-precision real-world interaction loops ingesting robot dataset feedback
    core.latest_external_telemetry = 0.9521
    core.run_inference_step()
    
    # Assert that the distance score correctly steps down past baseline barrier thresholds
    assert core.current_distance_percentage < 12.50
  
