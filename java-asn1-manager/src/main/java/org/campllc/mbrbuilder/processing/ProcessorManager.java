package org.campllc.mbrbuilder.processing;

import java.util.HashMap;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.stereotype.Service;

@Service
public class ProcessorManager {

	public static Map<ProcessingTypes,Class> processorMap = new HashMap<>();

	private ApplicationContext applicationContext;

	public ProcessorManager(@Autowired ApplicationContext applicationContext) {
		this.applicationContext = applicationContext;
	}

	public Processor getProcessor(ProcessingTypes processingType) {
		return applicationContext.getBean((Class<Processor>)processorMap.get(processingType));
	}
}
