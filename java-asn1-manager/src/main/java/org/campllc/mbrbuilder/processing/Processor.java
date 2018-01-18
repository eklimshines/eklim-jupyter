package org.campllc.mbrbuilder.processing;

public interface Processor {
	public ProcessingTypes getProcessorType();

	public void runProcess();
}
